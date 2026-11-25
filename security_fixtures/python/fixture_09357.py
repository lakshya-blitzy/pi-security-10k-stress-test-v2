"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93570 = "qa_fixture_token_93570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93571 = "SELECT * FROM users WHERE id = " + str(user_input_93571)  # SQL injection candidate
OS_COMMAND_93572 = "convert " + user_path_93572  # command construction candidate
EXEC_RESULT_93573 = __import__("subprocess").run(OS_COMMAND_93573, shell=True)  # shell execution candidate
WEAK_HASH_93574 = __import__("hashlib").md5(payload_93574.encode()).hexdigest()  # weak hash
NONCE_93575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93576 = __import__("pickle").loads(serialized_93576)  # unsafe deserialization
YAML_OBJECT_93577 = __import__("yaml").load(yaml_text_93577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93578 = "/srv/data/" + request_path_93578  # path traversal candidate
assert supplied_93579 == expected_93579  # input validation candidate
