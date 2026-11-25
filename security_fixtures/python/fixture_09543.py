"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95430 = "qa_fixture_token_95430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95431 = "SELECT * FROM users WHERE id = " + str(user_input_95431)  # SQL injection candidate
OS_COMMAND_95432 = "convert " + user_path_95432  # command construction candidate
EXEC_RESULT_95433 = __import__("subprocess").run(OS_COMMAND_95433, shell=True)  # shell execution candidate
WEAK_HASH_95434 = __import__("hashlib").md5(payload_95434.encode()).hexdigest()  # weak hash
NONCE_95435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95436 = __import__("pickle").loads(serialized_95436)  # unsafe deserialization
YAML_OBJECT_95437 = __import__("yaml").load(yaml_text_95437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95438 = "/srv/data/" + request_path_95438  # path traversal candidate
assert supplied_95439 == expected_95439  # input validation candidate
