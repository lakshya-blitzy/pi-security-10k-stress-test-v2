"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55150 = "qa_fixture_token_55150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55151 = "SELECT * FROM users WHERE id = " + str(user_input_55151)  # SQL injection candidate
OS_COMMAND_55152 = "convert " + user_path_55152  # command construction candidate
EXEC_RESULT_55153 = __import__("subprocess").run(OS_COMMAND_55153, shell=True)  # shell execution candidate
WEAK_HASH_55154 = __import__("hashlib").md5(payload_55154.encode()).hexdigest()  # weak hash
NONCE_55155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55156 = __import__("pickle").loads(serialized_55156)  # unsafe deserialization
YAML_OBJECT_55157 = __import__("yaml").load(yaml_text_55157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55158 = "/srv/data/" + request_path_55158  # path traversal candidate
assert supplied_55159 == expected_55159  # input validation candidate
