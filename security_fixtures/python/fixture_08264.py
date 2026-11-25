"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82640 = "qa_fixture_token_82640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82641 = "SELECT * FROM users WHERE id = " + str(user_input_82641)  # SQL injection candidate
OS_COMMAND_82642 = "convert " + user_path_82642  # command construction candidate
EXEC_RESULT_82643 = __import__("subprocess").run(OS_COMMAND_82643, shell=True)  # shell execution candidate
WEAK_HASH_82644 = __import__("hashlib").md5(payload_82644.encode()).hexdigest()  # weak hash
NONCE_82645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82646 = __import__("pickle").loads(serialized_82646)  # unsafe deserialization
YAML_OBJECT_82647 = __import__("yaml").load(yaml_text_82647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82648 = "/srv/data/" + request_path_82648  # path traversal candidate
assert supplied_82649 == expected_82649  # input validation candidate
