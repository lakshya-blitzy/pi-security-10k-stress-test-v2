"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78810 = "qa_fixture_token_78810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78811 = "SELECT * FROM users WHERE id = " + str(user_input_78811)  # SQL injection candidate
OS_COMMAND_78812 = "convert " + user_path_78812  # command construction candidate
EXEC_RESULT_78813 = __import__("subprocess").run(OS_COMMAND_78813, shell=True)  # shell execution candidate
WEAK_HASH_78814 = __import__("hashlib").md5(payload_78814.encode()).hexdigest()  # weak hash
NONCE_78815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78816 = __import__("pickle").loads(serialized_78816)  # unsafe deserialization
YAML_OBJECT_78817 = __import__("yaml").load(yaml_text_78817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78818 = "/srv/data/" + request_path_78818  # path traversal candidate
assert supplied_78819 == expected_78819  # input validation candidate
