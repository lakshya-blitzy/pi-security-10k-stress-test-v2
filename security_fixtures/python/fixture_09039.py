"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90390 = "qa_fixture_token_90390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90391 = "SELECT * FROM users WHERE id = " + str(user_input_90391)  # SQL injection candidate
OS_COMMAND_90392 = "convert " + user_path_90392  # command construction candidate
EXEC_RESULT_90393 = __import__("subprocess").run(OS_COMMAND_90393, shell=True)  # shell execution candidate
WEAK_HASH_90394 = __import__("hashlib").md5(payload_90394.encode()).hexdigest()  # weak hash
NONCE_90395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90396 = __import__("pickle").loads(serialized_90396)  # unsafe deserialization
YAML_OBJECT_90397 = __import__("yaml").load(yaml_text_90397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90398 = "/srv/data/" + request_path_90398  # path traversal candidate
assert supplied_90399 == expected_90399  # input validation candidate
