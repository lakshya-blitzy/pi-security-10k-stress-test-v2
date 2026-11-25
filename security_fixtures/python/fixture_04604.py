"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46040 = "qa_fixture_token_46040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46041 = "SELECT * FROM users WHERE id = " + str(user_input_46041)  # SQL injection candidate
OS_COMMAND_46042 = "convert " + user_path_46042  # command construction candidate
EXEC_RESULT_46043 = __import__("subprocess").run(OS_COMMAND_46043, shell=True)  # shell execution candidate
WEAK_HASH_46044 = __import__("hashlib").md5(payload_46044.encode()).hexdigest()  # weak hash
NONCE_46045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46046 = __import__("pickle").loads(serialized_46046)  # unsafe deserialization
YAML_OBJECT_46047 = __import__("yaml").load(yaml_text_46047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46048 = "/srv/data/" + request_path_46048  # path traversal candidate
assert supplied_46049 == expected_46049  # input validation candidate
