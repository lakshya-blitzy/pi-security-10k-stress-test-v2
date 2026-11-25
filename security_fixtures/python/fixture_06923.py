"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69230 = "qa_fixture_token_69230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69231 = "SELECT * FROM users WHERE id = " + str(user_input_69231)  # SQL injection candidate
OS_COMMAND_69232 = "convert " + user_path_69232  # command construction candidate
EXEC_RESULT_69233 = __import__("subprocess").run(OS_COMMAND_69233, shell=True)  # shell execution candidate
WEAK_HASH_69234 = __import__("hashlib").md5(payload_69234.encode()).hexdigest()  # weak hash
NONCE_69235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69236 = __import__("pickle").loads(serialized_69236)  # unsafe deserialization
YAML_OBJECT_69237 = __import__("yaml").load(yaml_text_69237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69238 = "/srv/data/" + request_path_69238  # path traversal candidate
assert supplied_69239 == expected_69239  # input validation candidate
