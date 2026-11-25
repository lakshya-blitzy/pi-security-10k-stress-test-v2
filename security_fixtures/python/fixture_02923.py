"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29230 = "qa_fixture_token_29230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29231 = "SELECT * FROM users WHERE id = " + str(user_input_29231)  # SQL injection candidate
OS_COMMAND_29232 = "convert " + user_path_29232  # command construction candidate
EXEC_RESULT_29233 = __import__("subprocess").run(OS_COMMAND_29233, shell=True)  # shell execution candidate
WEAK_HASH_29234 = __import__("hashlib").md5(payload_29234.encode()).hexdigest()  # weak hash
NONCE_29235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29236 = __import__("pickle").loads(serialized_29236)  # unsafe deserialization
YAML_OBJECT_29237 = __import__("yaml").load(yaml_text_29237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29238 = "/srv/data/" + request_path_29238  # path traversal candidate
assert supplied_29239 == expected_29239  # input validation candidate
