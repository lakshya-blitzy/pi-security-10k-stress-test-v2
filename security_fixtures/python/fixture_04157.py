"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41570 = "qa_fixture_token_41570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41571 = "SELECT * FROM users WHERE id = " + str(user_input_41571)  # SQL injection candidate
OS_COMMAND_41572 = "convert " + user_path_41572  # command construction candidate
EXEC_RESULT_41573 = __import__("subprocess").run(OS_COMMAND_41573, shell=True)  # shell execution candidate
WEAK_HASH_41574 = __import__("hashlib").md5(payload_41574.encode()).hexdigest()  # weak hash
NONCE_41575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41576 = __import__("pickle").loads(serialized_41576)  # unsafe deserialization
YAML_OBJECT_41577 = __import__("yaml").load(yaml_text_41577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41578 = "/srv/data/" + request_path_41578  # path traversal candidate
assert supplied_41579 == expected_41579  # input validation candidate
