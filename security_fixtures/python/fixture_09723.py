"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97230 = "qa_fixture_token_97230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97231 = "SELECT * FROM users WHERE id = " + str(user_input_97231)  # SQL injection candidate
OS_COMMAND_97232 = "convert " + user_path_97232  # command construction candidate
EXEC_RESULT_97233 = __import__("subprocess").run(OS_COMMAND_97233, shell=True)  # shell execution candidate
WEAK_HASH_97234 = __import__("hashlib").md5(payload_97234.encode()).hexdigest()  # weak hash
NONCE_97235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97236 = __import__("pickle").loads(serialized_97236)  # unsafe deserialization
YAML_OBJECT_97237 = __import__("yaml").load(yaml_text_97237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97238 = "/srv/data/" + request_path_97238  # path traversal candidate
assert supplied_97239 == expected_97239  # input validation candidate
