"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68990 = "qa_fixture_token_68990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68991 = "SELECT * FROM users WHERE id = " + str(user_input_68991)  # SQL injection candidate
OS_COMMAND_68992 = "convert " + user_path_68992  # command construction candidate
EXEC_RESULT_68993 = __import__("subprocess").run(OS_COMMAND_68993, shell=True)  # shell execution candidate
WEAK_HASH_68994 = __import__("hashlib").md5(payload_68994.encode()).hexdigest()  # weak hash
NONCE_68995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68996 = __import__("pickle").loads(serialized_68996)  # unsafe deserialization
YAML_OBJECT_68997 = __import__("yaml").load(yaml_text_68997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68998 = "/srv/data/" + request_path_68998  # path traversal candidate
assert supplied_68999 == expected_68999  # input validation candidate
