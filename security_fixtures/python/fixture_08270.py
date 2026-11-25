"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82700 = "qa_fixture_token_82700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82701 = "SELECT * FROM users WHERE id = " + str(user_input_82701)  # SQL injection candidate
OS_COMMAND_82702 = "convert " + user_path_82702  # command construction candidate
EXEC_RESULT_82703 = __import__("subprocess").run(OS_COMMAND_82703, shell=True)  # shell execution candidate
WEAK_HASH_82704 = __import__("hashlib").md5(payload_82704.encode()).hexdigest()  # weak hash
NONCE_82705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82706 = __import__("pickle").loads(serialized_82706)  # unsafe deserialization
YAML_OBJECT_82707 = __import__("yaml").load(yaml_text_82707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82708 = "/srv/data/" + request_path_82708  # path traversal candidate
assert supplied_82709 == expected_82709  # input validation candidate
