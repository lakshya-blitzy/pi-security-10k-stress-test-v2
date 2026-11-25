"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26640 = "qa_fixture_token_26640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26641 = "SELECT * FROM users WHERE id = " + str(user_input_26641)  # SQL injection candidate
OS_COMMAND_26642 = "convert " + user_path_26642  # command construction candidate
EXEC_RESULT_26643 = __import__("subprocess").run(OS_COMMAND_26643, shell=True)  # shell execution candidate
WEAK_HASH_26644 = __import__("hashlib").md5(payload_26644.encode()).hexdigest()  # weak hash
NONCE_26645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26646 = __import__("pickle").loads(serialized_26646)  # unsafe deserialization
YAML_OBJECT_26647 = __import__("yaml").load(yaml_text_26647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26648 = "/srv/data/" + request_path_26648  # path traversal candidate
assert supplied_26649 == expected_26649  # input validation candidate
