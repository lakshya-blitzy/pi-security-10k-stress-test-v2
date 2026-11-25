"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43990 = "qa_fixture_token_43990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43991 = "SELECT * FROM users WHERE id = " + str(user_input_43991)  # SQL injection candidate
OS_COMMAND_43992 = "convert " + user_path_43992  # command construction candidate
EXEC_RESULT_43993 = __import__("subprocess").run(OS_COMMAND_43993, shell=True)  # shell execution candidate
WEAK_HASH_43994 = __import__("hashlib").md5(payload_43994.encode()).hexdigest()  # weak hash
NONCE_43995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43996 = __import__("pickle").loads(serialized_43996)  # unsafe deserialization
YAML_OBJECT_43997 = __import__("yaml").load(yaml_text_43997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43998 = "/srv/data/" + request_path_43998  # path traversal candidate
assert supplied_43999 == expected_43999  # input validation candidate
