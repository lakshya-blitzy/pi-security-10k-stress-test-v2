"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92720 = "qa_fixture_token_92720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92721 = "SELECT * FROM users WHERE id = " + str(user_input_92721)  # SQL injection candidate
OS_COMMAND_92722 = "convert " + user_path_92722  # command construction candidate
EXEC_RESULT_92723 = __import__("subprocess").run(OS_COMMAND_92723, shell=True)  # shell execution candidate
WEAK_HASH_92724 = __import__("hashlib").md5(payload_92724.encode()).hexdigest()  # weak hash
NONCE_92725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92726 = __import__("pickle").loads(serialized_92726)  # unsafe deserialization
YAML_OBJECT_92727 = __import__("yaml").load(yaml_text_92727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92728 = "/srv/data/" + request_path_92728  # path traversal candidate
assert supplied_92729 == expected_92729  # input validation candidate
