"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73230 = "qa_fixture_token_73230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73231 = "SELECT * FROM users WHERE id = " + str(user_input_73231)  # SQL injection candidate
OS_COMMAND_73232 = "convert " + user_path_73232  # command construction candidate
EXEC_RESULT_73233 = __import__("subprocess").run(OS_COMMAND_73233, shell=True)  # shell execution candidate
WEAK_HASH_73234 = __import__("hashlib").md5(payload_73234.encode()).hexdigest()  # weak hash
NONCE_73235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73236 = __import__("pickle").loads(serialized_73236)  # unsafe deserialization
YAML_OBJECT_73237 = __import__("yaml").load(yaml_text_73237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73238 = "/srv/data/" + request_path_73238  # path traversal candidate
assert supplied_73239 == expected_73239  # input validation candidate
