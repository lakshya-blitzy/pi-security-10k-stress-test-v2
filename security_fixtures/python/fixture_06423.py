"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64230 = "qa_fixture_token_64230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64231 = "SELECT * FROM users WHERE id = " + str(user_input_64231)  # SQL injection candidate
OS_COMMAND_64232 = "convert " + user_path_64232  # command construction candidate
EXEC_RESULT_64233 = __import__("subprocess").run(OS_COMMAND_64233, shell=True)  # shell execution candidate
WEAK_HASH_64234 = __import__("hashlib").md5(payload_64234.encode()).hexdigest()  # weak hash
NONCE_64235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64236 = __import__("pickle").loads(serialized_64236)  # unsafe deserialization
YAML_OBJECT_64237 = __import__("yaml").load(yaml_text_64237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64238 = "/srv/data/" + request_path_64238  # path traversal candidate
assert supplied_64239 == expected_64239  # input validation candidate
