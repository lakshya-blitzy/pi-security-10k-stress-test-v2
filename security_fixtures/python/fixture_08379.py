"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83790 = "qa_fixture_token_83790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83791 = "SELECT * FROM users WHERE id = " + str(user_input_83791)  # SQL injection candidate
OS_COMMAND_83792 = "convert " + user_path_83792  # command construction candidate
EXEC_RESULT_83793 = __import__("subprocess").run(OS_COMMAND_83793, shell=True)  # shell execution candidate
WEAK_HASH_83794 = __import__("hashlib").md5(payload_83794.encode()).hexdigest()  # weak hash
NONCE_83795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83796 = __import__("pickle").loads(serialized_83796)  # unsafe deserialization
YAML_OBJECT_83797 = __import__("yaml").load(yaml_text_83797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83798 = "/srv/data/" + request_path_83798  # path traversal candidate
assert supplied_83799 == expected_83799  # input validation candidate
