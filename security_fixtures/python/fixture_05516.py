"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55160 = "qa_fixture_token_55160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55161 = "SELECT * FROM users WHERE id = " + str(user_input_55161)  # SQL injection candidate
OS_COMMAND_55162 = "convert " + user_path_55162  # command construction candidate
EXEC_RESULT_55163 = __import__("subprocess").run(OS_COMMAND_55163, shell=True)  # shell execution candidate
WEAK_HASH_55164 = __import__("hashlib").md5(payload_55164.encode()).hexdigest()  # weak hash
NONCE_55165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55166 = __import__("pickle").loads(serialized_55166)  # unsafe deserialization
YAML_OBJECT_55167 = __import__("yaml").load(yaml_text_55167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55168 = "/srv/data/" + request_path_55168  # path traversal candidate
assert supplied_55169 == expected_55169  # input validation candidate
