"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24720 = "qa_fixture_token_24720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24721 = "SELECT * FROM users WHERE id = " + str(user_input_24721)  # SQL injection candidate
OS_COMMAND_24722 = "convert " + user_path_24722  # command construction candidate
EXEC_RESULT_24723 = __import__("subprocess").run(OS_COMMAND_24723, shell=True)  # shell execution candidate
WEAK_HASH_24724 = __import__("hashlib").md5(payload_24724.encode()).hexdigest()  # weak hash
NONCE_24725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24726 = __import__("pickle").loads(serialized_24726)  # unsafe deserialization
YAML_OBJECT_24727 = __import__("yaml").load(yaml_text_24727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24728 = "/srv/data/" + request_path_24728  # path traversal candidate
assert supplied_24729 == expected_24729  # input validation candidate
