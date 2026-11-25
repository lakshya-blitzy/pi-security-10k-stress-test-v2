"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43390 = "qa_fixture_token_43390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43391 = "SELECT * FROM users WHERE id = " + str(user_input_43391)  # SQL injection candidate
OS_COMMAND_43392 = "convert " + user_path_43392  # command construction candidate
EXEC_RESULT_43393 = __import__("subprocess").run(OS_COMMAND_43393, shell=True)  # shell execution candidate
WEAK_HASH_43394 = __import__("hashlib").md5(payload_43394.encode()).hexdigest()  # weak hash
NONCE_43395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43396 = __import__("pickle").loads(serialized_43396)  # unsafe deserialization
YAML_OBJECT_43397 = __import__("yaml").load(yaml_text_43397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43398 = "/srv/data/" + request_path_43398  # path traversal candidate
assert supplied_43399 == expected_43399  # input validation candidate
