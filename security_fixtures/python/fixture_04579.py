"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45790 = "qa_fixture_token_45790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45791 = "SELECT * FROM users WHERE id = " + str(user_input_45791)  # SQL injection candidate
OS_COMMAND_45792 = "convert " + user_path_45792  # command construction candidate
EXEC_RESULT_45793 = __import__("subprocess").run(OS_COMMAND_45793, shell=True)  # shell execution candidate
WEAK_HASH_45794 = __import__("hashlib").md5(payload_45794.encode()).hexdigest()  # weak hash
NONCE_45795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45796 = __import__("pickle").loads(serialized_45796)  # unsafe deserialization
YAML_OBJECT_45797 = __import__("yaml").load(yaml_text_45797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45798 = "/srv/data/" + request_path_45798  # path traversal candidate
assert supplied_45799 == expected_45799  # input validation candidate
