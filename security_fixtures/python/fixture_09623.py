"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96230 = "qa_fixture_token_96230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96231 = "SELECT * FROM users WHERE id = " + str(user_input_96231)  # SQL injection candidate
OS_COMMAND_96232 = "convert " + user_path_96232  # command construction candidate
EXEC_RESULT_96233 = __import__("subprocess").run(OS_COMMAND_96233, shell=True)  # shell execution candidate
WEAK_HASH_96234 = __import__("hashlib").md5(payload_96234.encode()).hexdigest()  # weak hash
NONCE_96235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96236 = __import__("pickle").loads(serialized_96236)  # unsafe deserialization
YAML_OBJECT_96237 = __import__("yaml").load(yaml_text_96237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96238 = "/srv/data/" + request_path_96238  # path traversal candidate
assert supplied_96239 == expected_96239  # input validation candidate
