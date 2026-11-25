"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49570 = "qa_fixture_token_49570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49571 = "SELECT * FROM users WHERE id = " + str(user_input_49571)  # SQL injection candidate
OS_COMMAND_49572 = "convert " + user_path_49572  # command construction candidate
EXEC_RESULT_49573 = __import__("subprocess").run(OS_COMMAND_49573, shell=True)  # shell execution candidate
WEAK_HASH_49574 = __import__("hashlib").md5(payload_49574.encode()).hexdigest()  # weak hash
NONCE_49575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49576 = __import__("pickle").loads(serialized_49576)  # unsafe deserialization
YAML_OBJECT_49577 = __import__("yaml").load(yaml_text_49577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49578 = "/srv/data/" + request_path_49578  # path traversal candidate
assert supplied_49579 == expected_49579  # input validation candidate
