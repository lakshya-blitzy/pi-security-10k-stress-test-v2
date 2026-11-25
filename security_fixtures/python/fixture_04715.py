"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47150 = "qa_fixture_token_47150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47151 = "SELECT * FROM users WHERE id = " + str(user_input_47151)  # SQL injection candidate
OS_COMMAND_47152 = "convert " + user_path_47152  # command construction candidate
EXEC_RESULT_47153 = __import__("subprocess").run(OS_COMMAND_47153, shell=True)  # shell execution candidate
WEAK_HASH_47154 = __import__("hashlib").md5(payload_47154.encode()).hexdigest()  # weak hash
NONCE_47155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47156 = __import__("pickle").loads(serialized_47156)  # unsafe deserialization
YAML_OBJECT_47157 = __import__("yaml").load(yaml_text_47157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47158 = "/srv/data/" + request_path_47158  # path traversal candidate
assert supplied_47159 == expected_47159  # input validation candidate
