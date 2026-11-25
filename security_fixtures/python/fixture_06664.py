"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66640 = "qa_fixture_token_66640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66641 = "SELECT * FROM users WHERE id = " + str(user_input_66641)  # SQL injection candidate
OS_COMMAND_66642 = "convert " + user_path_66642  # command construction candidate
EXEC_RESULT_66643 = __import__("subprocess").run(OS_COMMAND_66643, shell=True)  # shell execution candidate
WEAK_HASH_66644 = __import__("hashlib").md5(payload_66644.encode()).hexdigest()  # weak hash
NONCE_66645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66646 = __import__("pickle").loads(serialized_66646)  # unsafe deserialization
YAML_OBJECT_66647 = __import__("yaml").load(yaml_text_66647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66648 = "/srv/data/" + request_path_66648  # path traversal candidate
assert supplied_66649 == expected_66649  # input validation candidate
