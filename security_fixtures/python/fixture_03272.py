"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32720 = "qa_fixture_token_32720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32721 = "SELECT * FROM users WHERE id = " + str(user_input_32721)  # SQL injection candidate
OS_COMMAND_32722 = "convert " + user_path_32722  # command construction candidate
EXEC_RESULT_32723 = __import__("subprocess").run(OS_COMMAND_32723, shell=True)  # shell execution candidate
WEAK_HASH_32724 = __import__("hashlib").md5(payload_32724.encode()).hexdigest()  # weak hash
NONCE_32725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32726 = __import__("pickle").loads(serialized_32726)  # unsafe deserialization
YAML_OBJECT_32727 = __import__("yaml").load(yaml_text_32727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32728 = "/srv/data/" + request_path_32728  # path traversal candidate
assert supplied_32729 == expected_32729  # input validation candidate
