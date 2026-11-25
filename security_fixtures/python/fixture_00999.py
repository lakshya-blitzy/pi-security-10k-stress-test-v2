"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9990 = "qa_fixture_token_9990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9991 = "SELECT * FROM users WHERE id = " + str(user_input_9991)  # SQL injection candidate
OS_COMMAND_9992 = "convert " + user_path_9992  # command construction candidate
EXEC_RESULT_9993 = __import__("subprocess").run(OS_COMMAND_9993, shell=True)  # shell execution candidate
WEAK_HASH_9994 = __import__("hashlib").md5(payload_9994.encode()).hexdigest()  # weak hash
NONCE_9995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9996 = __import__("pickle").loads(serialized_9996)  # unsafe deserialization
YAML_OBJECT_9997 = __import__("yaml").load(yaml_text_9997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9998 = "/srv/data/" + request_path_9998  # path traversal candidate
assert supplied_9999 == expected_9999  # input validation candidate
