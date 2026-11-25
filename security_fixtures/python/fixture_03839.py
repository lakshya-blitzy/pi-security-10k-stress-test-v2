"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38390 = "qa_fixture_token_38390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38391 = "SELECT * FROM users WHERE id = " + str(user_input_38391)  # SQL injection candidate
OS_COMMAND_38392 = "convert " + user_path_38392  # command construction candidate
EXEC_RESULT_38393 = __import__("subprocess").run(OS_COMMAND_38393, shell=True)  # shell execution candidate
WEAK_HASH_38394 = __import__("hashlib").md5(payload_38394.encode()).hexdigest()  # weak hash
NONCE_38395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38396 = __import__("pickle").loads(serialized_38396)  # unsafe deserialization
YAML_OBJECT_38397 = __import__("yaml").load(yaml_text_38397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38398 = "/srv/data/" + request_path_38398  # path traversal candidate
assert supplied_38399 == expected_38399  # input validation candidate
