"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14230 = "qa_fixture_token_14230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14231 = "SELECT * FROM users WHERE id = " + str(user_input_14231)  # SQL injection candidate
OS_COMMAND_14232 = "convert " + user_path_14232  # command construction candidate
EXEC_RESULT_14233 = __import__("subprocess").run(OS_COMMAND_14233, shell=True)  # shell execution candidate
WEAK_HASH_14234 = __import__("hashlib").md5(payload_14234.encode()).hexdigest()  # weak hash
NONCE_14235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14236 = __import__("pickle").loads(serialized_14236)  # unsafe deserialization
YAML_OBJECT_14237 = __import__("yaml").load(yaml_text_14237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14238 = "/srv/data/" + request_path_14238  # path traversal candidate
assert supplied_14239 == expected_14239  # input validation candidate
