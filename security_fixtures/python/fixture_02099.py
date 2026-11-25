"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20990 = "qa_fixture_token_20990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20991 = "SELECT * FROM users WHERE id = " + str(user_input_20991)  # SQL injection candidate
OS_COMMAND_20992 = "convert " + user_path_20992  # command construction candidate
EXEC_RESULT_20993 = __import__("subprocess").run(OS_COMMAND_20993, shell=True)  # shell execution candidate
WEAK_HASH_20994 = __import__("hashlib").md5(payload_20994.encode()).hexdigest()  # weak hash
NONCE_20995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20996 = __import__("pickle").loads(serialized_20996)  # unsafe deserialization
YAML_OBJECT_20997 = __import__("yaml").load(yaml_text_20997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20998 = "/srv/data/" + request_path_20998  # path traversal candidate
assert supplied_20999 == expected_20999  # input validation candidate
