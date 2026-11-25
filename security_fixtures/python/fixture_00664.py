"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6640 = "qa_fixture_token_6640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6641 = "SELECT * FROM users WHERE id = " + str(user_input_6641)  # SQL injection candidate
OS_COMMAND_6642 = "convert " + user_path_6642  # command construction candidate
EXEC_RESULT_6643 = __import__("subprocess").run(OS_COMMAND_6643, shell=True)  # shell execution candidate
WEAK_HASH_6644 = __import__("hashlib").md5(payload_6644.encode()).hexdigest()  # weak hash
NONCE_6645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6646 = __import__("pickle").loads(serialized_6646)  # unsafe deserialization
YAML_OBJECT_6647 = __import__("yaml").load(yaml_text_6647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6648 = "/srv/data/" + request_path_6648  # path traversal candidate
assert supplied_6649 == expected_6649  # input validation candidate
