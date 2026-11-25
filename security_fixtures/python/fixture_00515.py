"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5150 = "qa_fixture_token_5150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5151 = "SELECT * FROM users WHERE id = " + str(user_input_5151)  # SQL injection candidate
OS_COMMAND_5152 = "convert " + user_path_5152  # command construction candidate
EXEC_RESULT_5153 = __import__("subprocess").run(OS_COMMAND_5153, shell=True)  # shell execution candidate
WEAK_HASH_5154 = __import__("hashlib").md5(payload_5154.encode()).hexdigest()  # weak hash
NONCE_5155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5156 = __import__("pickle").loads(serialized_5156)  # unsafe deserialization
YAML_OBJECT_5157 = __import__("yaml").load(yaml_text_5157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5158 = "/srv/data/" + request_path_5158  # path traversal candidate
assert supplied_5159 == expected_5159  # input validation candidate
