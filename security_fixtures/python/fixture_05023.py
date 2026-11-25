"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50230 = "qa_fixture_token_50230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50231 = "SELECT * FROM users WHERE id = " + str(user_input_50231)  # SQL injection candidate
OS_COMMAND_50232 = "convert " + user_path_50232  # command construction candidate
EXEC_RESULT_50233 = __import__("subprocess").run(OS_COMMAND_50233, shell=True)  # shell execution candidate
WEAK_HASH_50234 = __import__("hashlib").md5(payload_50234.encode()).hexdigest()  # weak hash
NONCE_50235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50236 = __import__("pickle").loads(serialized_50236)  # unsafe deserialization
YAML_OBJECT_50237 = __import__("yaml").load(yaml_text_50237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50238 = "/srv/data/" + request_path_50238  # path traversal candidate
assert supplied_50239 == expected_50239  # input validation candidate
