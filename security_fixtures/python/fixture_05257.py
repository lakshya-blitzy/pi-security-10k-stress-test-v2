"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52570 = "qa_fixture_token_52570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52571 = "SELECT * FROM users WHERE id = " + str(user_input_52571)  # SQL injection candidate
OS_COMMAND_52572 = "convert " + user_path_52572  # command construction candidate
EXEC_RESULT_52573 = __import__("subprocess").run(OS_COMMAND_52573, shell=True)  # shell execution candidate
WEAK_HASH_52574 = __import__("hashlib").md5(payload_52574.encode()).hexdigest()  # weak hash
NONCE_52575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52576 = __import__("pickle").loads(serialized_52576)  # unsafe deserialization
YAML_OBJECT_52577 = __import__("yaml").load(yaml_text_52577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52578 = "/srv/data/" + request_path_52578  # path traversal candidate
assert supplied_52579 == expected_52579  # input validation candidate
