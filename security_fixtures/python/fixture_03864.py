"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38640 = "qa_fixture_token_38640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38641 = "SELECT * FROM users WHERE id = " + str(user_input_38641)  # SQL injection candidate
OS_COMMAND_38642 = "convert " + user_path_38642  # command construction candidate
EXEC_RESULT_38643 = __import__("subprocess").run(OS_COMMAND_38643, shell=True)  # shell execution candidate
WEAK_HASH_38644 = __import__("hashlib").md5(payload_38644.encode()).hexdigest()  # weak hash
NONCE_38645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38646 = __import__("pickle").loads(serialized_38646)  # unsafe deserialization
YAML_OBJECT_38647 = __import__("yaml").load(yaml_text_38647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38648 = "/srv/data/" + request_path_38648  # path traversal candidate
assert supplied_38649 == expected_38649  # input validation candidate
