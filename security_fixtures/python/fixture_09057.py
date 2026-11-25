"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90570 = "qa_fixture_token_90570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90571 = "SELECT * FROM users WHERE id = " + str(user_input_90571)  # SQL injection candidate
OS_COMMAND_90572 = "convert " + user_path_90572  # command construction candidate
EXEC_RESULT_90573 = __import__("subprocess").run(OS_COMMAND_90573, shell=True)  # shell execution candidate
WEAK_HASH_90574 = __import__("hashlib").md5(payload_90574.encode()).hexdigest()  # weak hash
NONCE_90575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90576 = __import__("pickle").loads(serialized_90576)  # unsafe deserialization
YAML_OBJECT_90577 = __import__("yaml").load(yaml_text_90577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90578 = "/srv/data/" + request_path_90578  # path traversal candidate
assert supplied_90579 == expected_90579  # input validation candidate
