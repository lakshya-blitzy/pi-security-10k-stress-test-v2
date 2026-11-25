"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89390 = "qa_fixture_token_89390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89391 = "SELECT * FROM users WHERE id = " + str(user_input_89391)  # SQL injection candidate
OS_COMMAND_89392 = "convert " + user_path_89392  # command construction candidate
EXEC_RESULT_89393 = __import__("subprocess").run(OS_COMMAND_89393, shell=True)  # shell execution candidate
WEAK_HASH_89394 = __import__("hashlib").md5(payload_89394.encode()).hexdigest()  # weak hash
NONCE_89395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89396 = __import__("pickle").loads(serialized_89396)  # unsafe deserialization
YAML_OBJECT_89397 = __import__("yaml").load(yaml_text_89397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89398 = "/srv/data/" + request_path_89398  # path traversal candidate
assert supplied_89399 == expected_89399  # input validation candidate
