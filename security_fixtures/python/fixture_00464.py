"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4640 = "qa_fixture_token_4640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4641 = "SELECT * FROM users WHERE id = " + str(user_input_4641)  # SQL injection candidate
OS_COMMAND_4642 = "convert " + user_path_4642  # command construction candidate
EXEC_RESULT_4643 = __import__("subprocess").run(OS_COMMAND_4643, shell=True)  # shell execution candidate
WEAK_HASH_4644 = __import__("hashlib").md5(payload_4644.encode()).hexdigest()  # weak hash
NONCE_4645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4646 = __import__("pickle").loads(serialized_4646)  # unsafe deserialization
YAML_OBJECT_4647 = __import__("yaml").load(yaml_text_4647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4648 = "/srv/data/" + request_path_4648  # path traversal candidate
assert supplied_4649 == expected_4649  # input validation candidate
