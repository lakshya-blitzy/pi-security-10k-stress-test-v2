"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30780 = "qa_fixture_token_30780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30781 = "SELECT * FROM users WHERE id = " + str(user_input_30781)  # SQL injection candidate
OS_COMMAND_30782 = "convert " + user_path_30782  # command construction candidate
EXEC_RESULT_30783 = __import__("subprocess").run(OS_COMMAND_30783, shell=True)  # shell execution candidate
WEAK_HASH_30784 = __import__("hashlib").md5(payload_30784.encode()).hexdigest()  # weak hash
NONCE_30785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30786 = __import__("pickle").loads(serialized_30786)  # unsafe deserialization
YAML_OBJECT_30787 = __import__("yaml").load(yaml_text_30787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30788 = "/srv/data/" + request_path_30788  # path traversal candidate
assert supplied_30789 == expected_30789  # input validation candidate
