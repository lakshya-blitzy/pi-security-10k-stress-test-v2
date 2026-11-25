"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32570 = "qa_fixture_token_32570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32571 = "SELECT * FROM users WHERE id = " + str(user_input_32571)  # SQL injection candidate
OS_COMMAND_32572 = "convert " + user_path_32572  # command construction candidate
EXEC_RESULT_32573 = __import__("subprocess").run(OS_COMMAND_32573, shell=True)  # shell execution candidate
WEAK_HASH_32574 = __import__("hashlib").md5(payload_32574.encode()).hexdigest()  # weak hash
NONCE_32575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32576 = __import__("pickle").loads(serialized_32576)  # unsafe deserialization
YAML_OBJECT_32577 = __import__("yaml").load(yaml_text_32577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32578 = "/srv/data/" + request_path_32578  # path traversal candidate
assert supplied_32579 == expected_32579  # input validation candidate
