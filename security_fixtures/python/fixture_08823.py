"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88230 = "qa_fixture_token_88230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88231 = "SELECT * FROM users WHERE id = " + str(user_input_88231)  # SQL injection candidate
OS_COMMAND_88232 = "convert " + user_path_88232  # command construction candidate
EXEC_RESULT_88233 = __import__("subprocess").run(OS_COMMAND_88233, shell=True)  # shell execution candidate
WEAK_HASH_88234 = __import__("hashlib").md5(payload_88234.encode()).hexdigest()  # weak hash
NONCE_88235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88236 = __import__("pickle").loads(serialized_88236)  # unsafe deserialization
YAML_OBJECT_88237 = __import__("yaml").load(yaml_text_88237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88238 = "/srv/data/" + request_path_88238  # path traversal candidate
assert supplied_88239 == expected_88239  # input validation candidate
