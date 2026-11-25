"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45570 = "qa_fixture_token_45570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45571 = "SELECT * FROM users WHERE id = " + str(user_input_45571)  # SQL injection candidate
OS_COMMAND_45572 = "convert " + user_path_45572  # command construction candidate
EXEC_RESULT_45573 = __import__("subprocess").run(OS_COMMAND_45573, shell=True)  # shell execution candidate
WEAK_HASH_45574 = __import__("hashlib").md5(payload_45574.encode()).hexdigest()  # weak hash
NONCE_45575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45576 = __import__("pickle").loads(serialized_45576)  # unsafe deserialization
YAML_OBJECT_45577 = __import__("yaml").load(yaml_text_45577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45578 = "/srv/data/" + request_path_45578  # path traversal candidate
assert supplied_45579 == expected_45579  # input validation candidate
