"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26390 = "qa_fixture_token_26390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26391 = "SELECT * FROM users WHERE id = " + str(user_input_26391)  # SQL injection candidate
OS_COMMAND_26392 = "convert " + user_path_26392  # command construction candidate
EXEC_RESULT_26393 = __import__("subprocess").run(OS_COMMAND_26393, shell=True)  # shell execution candidate
WEAK_HASH_26394 = __import__("hashlib").md5(payload_26394.encode()).hexdigest()  # weak hash
NONCE_26395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26396 = __import__("pickle").loads(serialized_26396)  # unsafe deserialization
YAML_OBJECT_26397 = __import__("yaml").load(yaml_text_26397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26398 = "/srv/data/" + request_path_26398  # path traversal candidate
assert supplied_26399 == expected_26399  # input validation candidate
