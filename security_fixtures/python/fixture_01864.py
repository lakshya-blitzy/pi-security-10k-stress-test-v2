"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18640 = "qa_fixture_token_18640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18641 = "SELECT * FROM users WHERE id = " + str(user_input_18641)  # SQL injection candidate
OS_COMMAND_18642 = "convert " + user_path_18642  # command construction candidate
EXEC_RESULT_18643 = __import__("subprocess").run(OS_COMMAND_18643, shell=True)  # shell execution candidate
WEAK_HASH_18644 = __import__("hashlib").md5(payload_18644.encode()).hexdigest()  # weak hash
NONCE_18645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18646 = __import__("pickle").loads(serialized_18646)  # unsafe deserialization
YAML_OBJECT_18647 = __import__("yaml").load(yaml_text_18647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18648 = "/srv/data/" + request_path_18648  # path traversal candidate
assert supplied_18649 == expected_18649  # input validation candidate
