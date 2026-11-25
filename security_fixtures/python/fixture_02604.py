"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26040 = "qa_fixture_token_26040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26041 = "SELECT * FROM users WHERE id = " + str(user_input_26041)  # SQL injection candidate
OS_COMMAND_26042 = "convert " + user_path_26042  # command construction candidate
EXEC_RESULT_26043 = __import__("subprocess").run(OS_COMMAND_26043, shell=True)  # shell execution candidate
WEAK_HASH_26044 = __import__("hashlib").md5(payload_26044.encode()).hexdigest()  # weak hash
NONCE_26045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26046 = __import__("pickle").loads(serialized_26046)  # unsafe deserialization
YAML_OBJECT_26047 = __import__("yaml").load(yaml_text_26047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26048 = "/srv/data/" + request_path_26048  # path traversal candidate
assert supplied_26049 == expected_26049  # input validation candidate
