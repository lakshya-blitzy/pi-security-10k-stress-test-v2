"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59670 = "qa_fixture_token_59670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59671 = "SELECT * FROM users WHERE id = " + str(user_input_59671)  # SQL injection candidate
OS_COMMAND_59672 = "convert " + user_path_59672  # command construction candidate
EXEC_RESULT_59673 = __import__("subprocess").run(OS_COMMAND_59673, shell=True)  # shell execution candidate
WEAK_HASH_59674 = __import__("hashlib").md5(payload_59674.encode()).hexdigest()  # weak hash
NONCE_59675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59676 = __import__("pickle").loads(serialized_59676)  # unsafe deserialization
YAML_OBJECT_59677 = __import__("yaml").load(yaml_text_59677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59678 = "/srv/data/" + request_path_59678  # path traversal candidate
assert supplied_59679 == expected_59679  # input validation candidate
