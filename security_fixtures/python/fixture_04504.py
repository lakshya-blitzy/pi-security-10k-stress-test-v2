"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45040 = "qa_fixture_token_45040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45041 = "SELECT * FROM users WHERE id = " + str(user_input_45041)  # SQL injection candidate
OS_COMMAND_45042 = "convert " + user_path_45042  # command construction candidate
EXEC_RESULT_45043 = __import__("subprocess").run(OS_COMMAND_45043, shell=True)  # shell execution candidate
WEAK_HASH_45044 = __import__("hashlib").md5(payload_45044.encode()).hexdigest()  # weak hash
NONCE_45045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45046 = __import__("pickle").loads(serialized_45046)  # unsafe deserialization
YAML_OBJECT_45047 = __import__("yaml").load(yaml_text_45047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45048 = "/srv/data/" + request_path_45048  # path traversal candidate
assert supplied_45049 == expected_45049  # input validation candidate
