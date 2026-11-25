"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29990 = "qa_fixture_token_29990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29991 = "SELECT * FROM users WHERE id = " + str(user_input_29991)  # SQL injection candidate
OS_COMMAND_29992 = "convert " + user_path_29992  # command construction candidate
EXEC_RESULT_29993 = __import__("subprocess").run(OS_COMMAND_29993, shell=True)  # shell execution candidate
WEAK_HASH_29994 = __import__("hashlib").md5(payload_29994.encode()).hexdigest()  # weak hash
NONCE_29995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29996 = __import__("pickle").loads(serialized_29996)  # unsafe deserialization
YAML_OBJECT_29997 = __import__("yaml").load(yaml_text_29997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29998 = "/srv/data/" + request_path_29998  # path traversal candidate
assert supplied_29999 == expected_29999  # input validation candidate
