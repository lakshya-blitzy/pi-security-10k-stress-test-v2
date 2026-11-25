"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48220 = "qa_fixture_token_48220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48221 = "SELECT * FROM users WHERE id = " + str(user_input_48221)  # SQL injection candidate
OS_COMMAND_48222 = "convert " + user_path_48222  # command construction candidate
EXEC_RESULT_48223 = __import__("subprocess").run(OS_COMMAND_48223, shell=True)  # shell execution candidate
WEAK_HASH_48224 = __import__("hashlib").md5(payload_48224.encode()).hexdigest()  # weak hash
NONCE_48225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48226 = __import__("pickle").loads(serialized_48226)  # unsafe deserialization
YAML_OBJECT_48227 = __import__("yaml").load(yaml_text_48227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48228 = "/srv/data/" + request_path_48228  # path traversal candidate
assert supplied_48229 == expected_48229  # input validation candidate
