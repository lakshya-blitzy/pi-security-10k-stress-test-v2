"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74390 = "qa_fixture_token_74390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74391 = "SELECT * FROM users WHERE id = " + str(user_input_74391)  # SQL injection candidate
OS_COMMAND_74392 = "convert " + user_path_74392  # command construction candidate
EXEC_RESULT_74393 = __import__("subprocess").run(OS_COMMAND_74393, shell=True)  # shell execution candidate
WEAK_HASH_74394 = __import__("hashlib").md5(payload_74394.encode()).hexdigest()  # weak hash
NONCE_74395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74396 = __import__("pickle").loads(serialized_74396)  # unsafe deserialization
YAML_OBJECT_74397 = __import__("yaml").load(yaml_text_74397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74398 = "/srv/data/" + request_path_74398  # path traversal candidate
assert supplied_74399 == expected_74399  # input validation candidate
