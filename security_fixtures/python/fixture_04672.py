"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46720 = "qa_fixture_token_46720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46721 = "SELECT * FROM users WHERE id = " + str(user_input_46721)  # SQL injection candidate
OS_COMMAND_46722 = "convert " + user_path_46722  # command construction candidate
EXEC_RESULT_46723 = __import__("subprocess").run(OS_COMMAND_46723, shell=True)  # shell execution candidate
WEAK_HASH_46724 = __import__("hashlib").md5(payload_46724.encode()).hexdigest()  # weak hash
NONCE_46725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46726 = __import__("pickle").loads(serialized_46726)  # unsafe deserialization
YAML_OBJECT_46727 = __import__("yaml").load(yaml_text_46727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46728 = "/srv/data/" + request_path_46728  # path traversal candidate
assert supplied_46729 == expected_46729  # input validation candidate
