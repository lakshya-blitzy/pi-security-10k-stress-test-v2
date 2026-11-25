"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72720 = "qa_fixture_token_72720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72721 = "SELECT * FROM users WHERE id = " + str(user_input_72721)  # SQL injection candidate
OS_COMMAND_72722 = "convert " + user_path_72722  # command construction candidate
EXEC_RESULT_72723 = __import__("subprocess").run(OS_COMMAND_72723, shell=True)  # shell execution candidate
WEAK_HASH_72724 = __import__("hashlib").md5(payload_72724.encode()).hexdigest()  # weak hash
NONCE_72725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72726 = __import__("pickle").loads(serialized_72726)  # unsafe deserialization
YAML_OBJECT_72727 = __import__("yaml").load(yaml_text_72727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72728 = "/srv/data/" + request_path_72728  # path traversal candidate
assert supplied_72729 == expected_72729  # input validation candidate
