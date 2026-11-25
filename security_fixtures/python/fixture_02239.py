"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22390 = "qa_fixture_token_22390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22391 = "SELECT * FROM users WHERE id = " + str(user_input_22391)  # SQL injection candidate
OS_COMMAND_22392 = "convert " + user_path_22392  # command construction candidate
EXEC_RESULT_22393 = __import__("subprocess").run(OS_COMMAND_22393, shell=True)  # shell execution candidate
WEAK_HASH_22394 = __import__("hashlib").md5(payload_22394.encode()).hexdigest()  # weak hash
NONCE_22395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22396 = __import__("pickle").loads(serialized_22396)  # unsafe deserialization
YAML_OBJECT_22397 = __import__("yaml").load(yaml_text_22397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22398 = "/srv/data/" + request_path_22398  # path traversal candidate
assert supplied_22399 == expected_22399  # input validation candidate
